import { useEffect, useState } from 'react'
import './styles/Map.css'


const Map = ({ pName, pGender, bedNo }) => {
    const [patientsList, setPatientsList] = useState([]);
    
    useEffect(() => {
        if (pName && pGender && bedNo){
            const buttons = document.querySelectorAll('button');
            const bed = buttons[bedNo-1];
            bed.style.backgroundColor = 'red';
            // setPatientsList(patientsList => [...patientsList, {"pName": locationData[0], 'pGender': locationData[1],'bed_no': locationData[2]}]);
        }

    }, [pName, pGender, bedNo])

    
    return (
        <div>
            <div className='container'>
                 <div className="background-image">
                    <button className='bed-label1'>1</button>
                    <button className='bed-label2'>2</button>
                    <button className='bed-label3'>3</button>
                    <button className='bed-label4'>4</button>
                    <button className='bed-label5'>5</button>
                    <button className='bed-label6'>6</button>
                    <button className='bed-label7'>7</button>
                    <button className='bed-label8'>8</button>
                    <button className='bed-label9'>9</button>
                    <button className='bed-label10'>10</button>
                    <button className='bed-label11'>11</button>
                    <button className='bed-label12'>12</button>
                    <button className='bed-label13'>13</button>
                    <button className='bed-label14'>14</button>
                    <button className='bed-label15'>15</button>
                    <button className='bed-label16'>16</button>
                    <button className='bed-label17'>17</button>
                    <button className='bed-label18'>18</button>
                    <button className='bed-label19'>19</button>
                    <button className='bed-label20'>20</button>
                    <button className='bed-label21'>21</button>
                    <button className='legend' id='red'>Occupied</button>
                    <button className='legend' id='white'>Vacant</button>
                    <button className='legend' id='yellow'>Needs Cleaning</button>
                </div>
            </div>
                <a href="/"><button>Return to Homepage</button></a>   
        </div>
    )
}

export default Map
