import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';

import Axios from 'axios';




function App() {
  const [ImageSelected, setImageSelected] = useState(0);
  const [Class ,setClass] = useState();
    const uploadImage =  () => {
      const formData = new FormData()
      formData.append("file",ImageSelected)
      formData.append("upload_presets","sdifdf")
      Axios.post("http://127.0.0.1:8000/predict",formData).then((res) => {setClass(res.data.class)})
    };
  if(Class == "with_mask"){
  return (
    <div className="App">
        <h1>Target is wearing a mask</h1>
        <button onClick = {() => {setClass(0)}}>Reset</button>
    </div>
  );

     }

    else if(Class == "without_mask"){
      return (
        <div className="App">
            <h1>Target is not wearing a mask</h1>
            <button onClick = {() => {setClass(0)}}>Reset</button>
        </div>
      );

    }
    else{
      return (
      <div className="App">
        <input type = "file" onChange = {(event) => {
          setImageSelected(event.target.files[0])
        }}/>
        <button onClick = {uploadImage}>Upload</button>
    </div>
    )}
}

export default App;
