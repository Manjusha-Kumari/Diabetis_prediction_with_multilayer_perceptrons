import React from 'react';

const FormComponent = ({ handleSubmit, handleChange, formData }) => {
  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="pregnancies">Pregnancies</label>
        <input 
          type="number" 
          id="pregnancies" 
          name="pregnancies" 
          onChange={handleChange} 
          value={formData.pregnancies} 
          placeholder="Enter number of pregnancies"
        />
      </div>
      <div>
        <label htmlFor="glucose">Glucose</label>
        <input 
          type="number" 
          id="glucose" 
          name="glucose" 
          onChange={handleChange} 
          value={formData.glucose} 
          placeholder="Enter glucose level"
        />
      </div>
      <div>
        <label htmlFor="bloodPressure">Blood Pressure</label>
        <input 
          type="number" 
          id="bloodPressure" 
          name="bloodPressure" 
          onChange={handleChange} 
          value={formData.bloodPressure} 
          placeholder="Enter blood pressure"
        />
      </div>
      <div>
        <label htmlFor="skinThickness">Skin Thickness</label>
        <input 
          type="number" 
          id="skinThickness" 
          name="skinThickness" 
          onChange={handleChange} 
          value={formData.skinThickness} 
          placeholder="Enter skin thickness"
        />
      </div>
      <div>
        <label htmlFor="insulin">Insulin</label>
        <input 
          type="number" 
          id="insulin" 
          name="insulin" 
          onChange={handleChange} 
          value={formData.insulin} 
          placeholder="Enter insulin level"
        />
      </div>
      <div>
        <label htmlFor="bmi">BMI</label>
        <input 
          type="number" 
          id="bmi" 
          name="bmi" 
          onChange={handleChange} 
          value={formData.bmi} 
          placeholder="Enter BMI"
        />
      </div>
      <div>
        <label htmlFor="diabetesPedigreeFunction">Diabetes Pedigree Function</label>
        <input 
          type="number" 
          id="diabetesPedigreeFunction" 
          name="diabetesPedigreeFunction" 
          onChange={handleChange} 
          value={formData.diabetesPedigreeFunction} 
          placeholder="Enter diabetes pedigree function"
        />
      </div>
      <div>
        <label htmlFor="age">Age</label>
        <input 
          type="number" 
          id="age" 
          name="age" 
          onChange={handleChange} 
          value={formData.age} 
          placeholder="Enter age"
        />
      </div>
      <button type="submit" onClick={handleSubmit}>Predict Diabetes</button>
    </form>
  );
};

export default FormComponent;
