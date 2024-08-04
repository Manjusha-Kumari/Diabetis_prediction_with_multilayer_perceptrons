import React, { useState, useEffect } from 'react';
import axios from 'axios';
import FormComponent from './components/FormComponent';
import ImageComponent from './components/ImageComponent';
import './index.css';

function App() {
  const [formData, setFormData] = useState({
    pregnancies: '',
    glucose: '',
    bloodPressure: '',
    skinThickness: '',
    insulin: '',
    bmi: '',
    diabetesPedigreeFunction: '',
    age: ''
  });
  const [prediction, setPrediction] = useState(null);
  const [imageSrc, setImageSrc] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/predict', formData);
      setPrediction(response.data.prediction);
    } catch (error) {
      console.error('There was an error making the prediction!', error);
    }
  };

  useEffect(() => {
    const images = [
      '/assets/image1.png',
      '/assets/image2.png',
      '/assets/image3.png',
      '/assets/image4.png',
      '/assets/image5.png',
    ];
    const randomIndex = Math.floor(Math.random() * images.length);
    setImageSrc(images[randomIndex]);
  }, []); // The empty dependency array ensures this runs only once when the component mounts

  return (
    <div className="app-container">
      <h1>Diabetes Predictor</h1>
      <div className="content-container">
        <div className="form-container">
          <FormComponent handleSubmit={handleSubmit} handleChange={handleChange} formData={formData} />
          {prediction !== null && (
            <div>
              <h2>Prediction: {prediction}</h2>
            </div>
          )}
        </div>
        <div className="image-container">
          <MemoizedImageComponent src={imageSrc} alt="Diabetes prediction illustration" />
        </div>
      </div>
    </div>
  );
}

const MemoizedImageComponent = React.memo(ImageComponent);

export default App;
