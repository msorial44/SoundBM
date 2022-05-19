#![cfg_attr(
  all(not(debug_assertions), target_os = "windows"),
  windows_subsystem = "windows"
)]

use rodio::*;
use rodio::cpal::traits::{HostTrait,DeviceTrait};


fn main() {
  tauri::Builder::default()
    .invoke_handler(tauri::generate_handler![list_devices])
    .run(tauri::generate_context!())
    .expect("error while running tauri application");
}

#[tauri::command]
fn list_devices() -> String {
  let host = cpal::default_host();
  let devices = host.input_devices().unwrap();
  let mut device_names = String::new();
  for device in devices{ 
     let dev:rodio::Device = device.into();
     let dev_name:String=dev.name().unwrap();
     device_names.push_str(&dev_name);
     device_names.push_str(",");
  }
  device_names.into()
}



