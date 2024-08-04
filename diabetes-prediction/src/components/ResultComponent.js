import React from 'react';

const ResultComponent = ({ prediction, formData }) => {
  return (
    <div>
      <h2>Prediction: {prediction}</h2>
      <h3>Entered Data:</h3>
      {Object.keys(formData).map((key) => (
        <div key={key}>
          <strong>{key.charAt(0).toUpperCase() + key.slice(1)}:</strong> {formData[key]}
        </div>
      ))}
    </div>
  );
};

export default ResultComponent;
