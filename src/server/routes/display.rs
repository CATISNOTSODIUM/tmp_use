use axum::{response::IntoResponse,http::StatusCode};
use std::fs::File;
use std::io::Read;


pub async fn display_tree()-> impl IntoResponse {
    let mut file = File::open("templates/sample1.json").expect("Cannot open file");
    let mut data = String::new();
    file.read_to_string(&mut data).unwrap();
    let json_value: serde_json::Value = serde_json::from_str(&data[..]).expect("JSON was not well-formatted");
    let pretty_json = serde_json::to_string_pretty(&json_value).unwrap();
    (StatusCode::OK, pretty_json.to_string())
}