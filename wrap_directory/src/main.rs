use std::{fs, path::{Path, PathBuf}};
use std::env::current_dir;

fn main() {
    //get project root and important paths
    let my_root = project_root::get_project_root().unwrap();
    let wrap_input_dir = my_root.join("wrap_input");
    
    let paths = fs::read_dir(wrap_input_dir).unwrap();

    //clear asset directory
    let assets_dir = my_root.join("assets");
    let assets_path = assets_dir.clone().into_os_string().into_string().unwrap();
    fs::remove_dir_all(assets_path.clone()).and_then(|_| fs::create_dir(assets_path.clone())).unwrap();
    println!("ASSET PATH {}",&assets_path);
    for path in paths {
        let path_tmp = path.unwrap();
        //read files
        let file_dir_parse =  path_tmp.path().into_os_string().into_string().unwrap();
        let file_name = path_tmp.file_name().into_string().unwrap();
        //split into four sections: course_name (String), skillset (u32), skill (u32), and normal file name (String).
        let parts: Vec<_> = file_name.split('_').collect();
        //check if filename has all four arguments.
        //example of invalid filename: ALG-005_10X_428_Content.md
        assert_eq!(parts.len(),4, "Invalid file name: {}\n", &file_name);
        //parse name
        let course_name = String::from(parts[0].clone());
        let skillset = parts[1].clone().parse::<u32>().expect(format!("Invalid skillset id at {}. The data must be in u32.\n", &file_name).as_str());
        let skill = parts[2].clone().parse::<u32>().expect(format!("Invalid skillset id at {}. The data must be in u32.\n", &file_name).as_str());
        let core_name = parts[3].clone();
        

        //rename directory
        let folder_dir_tmp = Path::new(&assets_path[..])
        .join(course_name) //course name 
        .join([parts[0],parts[1]].join("_"))  //skillset
        .join([parts[0],parts[1], parts[2]].join("_")); //skills

        let folder_dir = folder_dir_tmp.clone().into_os_string().into_string().unwrap();
        let file_dir = folder_dir_tmp.join(file_name).into_os_string().into_string().unwrap(); //file name

        fs::create_dir_all(folder_dir).expect("DIR");
        fs::copy(file_dir_parse, file_dir).expect("cannot create file");

    }
}
