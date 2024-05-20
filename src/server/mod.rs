use axum::{http::StatusCode, response::IntoResponse, routing::{get,get_service}, Json, Router};
use std::net::SocketAddr;
use axum_server::{bind};
use tower_http::cors::{Any, CorsLayer};
use axum::http::{Request, Response, Method, header, Uri};
use axum::body::{boxed, Body, BoxBody};
use tower_http::services::ServeDir;


pub mod routes;


pub async fn initialize_server(){

    //Initialize middleware CORS Layer
    let cors = CorsLayer::new() 
    .allow_methods([Method::GET, Method::POST])
    .allow_origin(tower_http::cors::Any);

    let service = ServeDir::new("assets");
    let app = Router::new()
    .route("/", get(|| async { "root" }))
    //retrieve files from src/tests
    .route("/receiver/:file_name", get(routes::send_data::stream_data))
    .route("/tree_raw", get(routes::display::display_tree))
    .nest_service("/tree",service)
	.layer(cors);

    //bind with port 3000
    axum::Server::bind(&"0.0.0.0:3000".parse().unwrap())
        .serve(app.into_make_service())
        .await
        .unwrap();
    
}
