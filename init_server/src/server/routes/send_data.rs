use axum::{extract::Path, http::StatusCode, response::IntoResponse, routing::get, Json, Router };
use serde::Deserialize;
use std::net::SocketAddr;
use axum_server::{bind};
use tower_http::cors::{Any, CorsLayer};
use axum::http::{Request, Response, Method, header, Uri};
use markdown_parser::{
    read_file, Error
};
use axum::extract::Query;
use std::fs;
use std::env;
use tokio::fs::File;
use std::path::PathBuf;
//for streaming
use axum::body::StreamBody;
use tokio_util::io::ReaderStream;
//for parsing markdown file
use pulldown_cmark::{Parser, Options};

#[derive(Deserialize)]
pub struct File_data {
    name: String,
}


pub async fn stream_data(file_query: Query<File_data>) -> impl IntoResponse {
    //get root
    let my_root = project_root::get_project_root().unwrap();
   

    let file_query = file_query.0;
    let file_data = file_query.name;
    let path = my_root.join("assets").join(file_data.clone());
    let file = File::open(path.clone()).await.unwrap();
    println!("Display from {}",path.display());
    

    let stream = ReaderStream::new(file);

    //define body
    let body = StreamBody::new(stream);

    //define header
    let content_type = match mime_guess::from_path(path.clone()).first_raw(){
        Some(x) => x,
        None => "text/plain",
    };
    println!("content type: {}", content_type);

    let headers = [
        (header::CONTENT_TYPE, content_type),
        (header::CONTENT_DISPOSITION,
        &format!("inline; filename=\" {} \"", file_data.clone()))
    ];

    

    //send data
    (headers, body).into_response()
}