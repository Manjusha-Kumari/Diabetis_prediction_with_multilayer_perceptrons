import React from 'react';

const images = [
  './assets/image_1.png',
  './assets/image_2.png',
  './assets/image_3.png',
  './assets/image_4.png',
  './assets/image_5.png',
];

const getRandomImage = () => {
  const randomIndex = Math.floor(Math.random() * images.length);
  return images[randomIndex];
};

const ImageComponent = () => {
  return (
    <div className="image-container">
      <img src={getRandomImage()} alt="Diabetes prediction illustration" />
    </div>
  );
};

export default ImageComponent;
