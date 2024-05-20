use axum::{response::IntoResponse,http::StatusCode};
use std::fs::File;
use std::io::Read;


pub async fn display_tree()-> impl IntoResponse {
    //get project root 
    let my_root = project_root::get_project_root().unwrap();
    let target_dir = my_root.join("templates/sample1.json");
    let mut file = File::open(target_dir).expect("Cannot open file");
    let mut data = String::new();
    file.read_to_string(&mut data).unwrap();
    //let yaml_read =  serde_yaml::to_string(&data[..]).expect("YAML file was not well-formatted");
    let res: serde_json::Value = serde_json::from_str(data.as_str()).expect("Cannot read json");
    let body = serde_json::to_string_pretty(&res).unwrap();
    (StatusCode::OK, body)
}