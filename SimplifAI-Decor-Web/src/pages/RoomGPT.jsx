import React, { useState } from "react";
import ImageSlider from "react-image-comparison-slider";
import Fade from "react-reveal/Fade";

const RoomGPT = () => {
  const [previewImage, setPreviewImage] = useState(null);
  const [newImage, setNewImage] = useState(null);
  const [prompt, setPrompt] = useState("");
  const [loadingTime, setLoadingTime] = useState(0);
  const [submitClicked, setSubmitClicked] = useState(false);

  const url = "http://127.0.0.1:8000/login/ml-model/";

  const handleImageUpload = (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = () => {
      setPreviewImage(reader.result);
    };

    reader.readAsDataURL(file);
  };

  const requestOptions = {
    method: "POST",
    body: JSON.stringify({ image: previewImage, prompt: prompt }),
  };

  const handleSubmit = async () => {
    try {
      const res = await fetch(url, requestOptions);
      const data = await res.json();
      setNewImage(data.image);
      setLoadingTime(parseInt(data.loading_time));
    } catch (error) {
      alert(error);
    }
  };

  return (
    <div style={{ marginLeft: "20px",padding:"100px" }}>
      <h1>RoomGPT</h1>
      <Fade bottom cascade>
        <h1 className="m-3" style={{fontSize : "25px",marginBottom:"20px"}} >Image Preview</h1>
        <div className="avatar">
          {previewImage ? (
            <>
              <img
                src={previewImage}
                alt="preview"
                style={{ width: "400px", marginLeft: "25px" }}
              />
              <input
                type="file"
                accept="image/*"
                className="form-control m-3"
                onChange={handleImageUpload}
              ></input>
            </>
          ) : (
            <><h1> </h1>
              <h1 className="m-3" style={{fontSize : "25px", paddingbottom: "200"}}>Upload Image</h1>
              <input
                type="file"
                accept="image/*"
                className="form-control m-3"
                style={{width:"400px", borderRadius: "5px", border: "1px solid #000"}}
                onChange={handleImageUpload}
              ></input>
            </>
          )}
        </div>
        <div>   </div>
        <h1 className="m-3" style={{ fontSize: "25px" }}>
          Prompt here
        </h1>
        <input
          type="text"
          placeholder="Eg: 'I want to redesign my room in rajasthani style'"
          className="form-control m-3"
          style={{width:"400px", borderRadius: "5px", border: "1px solid #000"}}
          onChange={(e) => setPrompt(e.target.value)}
        />
        <button
          className="btn btn-main"
          name="submit"
          type="submit"
          style={{ marginLeft: "19px" }}
          onClick={(e) => {
            e.preventDefault();
            setSubmitClicked(true);
            handleSubmit();
          }}
        >
          Submit
        </button>
      </Fade>

      {/* <img src={newImage} alt="newImage" /> */}

      <Fade bottom cascade>
        <div>  </div>
        <div>  </div>
        <div style={{ width: 700, height: 450, marginBottom: "60px" }}>
          <h1 className="m-3" style={{fontSize : "25px"}} >Slider Comparison</h1>
          {newImage ? (
            <ImageSlider image1={previewImage} image2={newImage} />
          ) : null}
        </div>
      </Fade>
    </div>
  );
};

export default RoomGPT;