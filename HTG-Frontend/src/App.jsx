import { useState } from 'react'
import './App.css'

function App() {

  return (
    <>
      <div className="title">
        <h3>ABC Hospital</h3>
        <h1>Bed Allocation System</h1>
      </div>
      <div>
      <a href="/patient-info"><button className="addPatientButton">Add Patient</button></a>
      </div>
      <div>
      <button className="seeMapButton">See Map</button>
      </div>
    </>
  )
}

export default App
