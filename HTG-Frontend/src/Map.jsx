import { useEffect, useState } from 'react'
import './styles/Map.css'
import axios from 'axios';


const Map = ({ pName, pGender, pAge, bedNo }) => {
    const [patientsList, setPatientsList] = useState({});
    const [isPopupVisible, setIsPopupVisible] = useState(false);
    const [selectedBed, setSelectedBed] = useState(null);
    
    useEffect(() => {
        setPatientsList(() => {
            let newList = {};
            for(let i = 1; i<22; i++){
                newList[i] = {pName: null, pGender: null, pAge: null, status: 'Vacant and Clean'}
            }
            return newList;
        });
        
    }, [])

    useEffect(() => {
        console.log(pName);
        if (pName && pGender && bedNo){
            const buttons = document.querySelectorAll('button');
            const bed = buttons[bedNo]; //Selecting all buttons also selects the submit button... so we don't subtract one any more
            bed.style.backgroundColor = 'red';
            setPatientsList(patientsList => {
                return {
                    ...patientsList,
                    [bedNo]: {pName, pGender, pAge, status: 'Occupied'}
                };
            });
        }

    }, [bedNo])

    const handleBedClick = (bedNumber) => {
        setSelectedBed(bedNumber);
        setIsPopupVisible(true);
    };

    const closePopup = () => {
        setIsPopupVisible(false);
    };

    const markForCleaning = (bedNumber) => {
        const buttons = document.querySelectorAll('button');
        const bed = buttons[bedNumber];
        bed.style.backgroundColor = 'yellow';
        setPatientsList(patientsList => {
            return {
                ...patientsList, 
                [bedNumber]: {pName: '', pGender: '', pAge: null, status: 'Needs Cleaning'}
            }
        });
    }

    const postData = async (bedNumber) => {
        try {
            const response = await axios.post('http://127.0.0.1:5000/free-bed', JSON.stringify(bedNumber), {
                    headers: { 'Content-Type': 'application/json'},
                });
            return response.data;
        } catch (error) {
            console.error("error posting to backend")
        }
    }

    const endCleaning = async (bedNumber) => {
        const buttons = document.querySelectorAll('button');
        const bed = buttons[bedNumber];
        bed.style.backgroundColor = 'white';
        const response = await postData(bedNumber);

        setPatientsList(patientsList => {
            return {
                ...patientsList, 
                [bedNumber]: {pName: '', pGender: '', pAge: null, status: 'Vacant and Clean'}
            }
        });
    }

    
    return (
        <div>
            <div className='container'>
                 <div className="background-image">
                 {[...Array(21)].map((_, index) => (
                        <button
                            key={index}
                            className={`bed-label${index + 1}`}
                            onClick={() => handleBedClick(index + 1)}
                        >
                            {index + 1}
                        </button>
                    ))}
                    <button className='legend' id='red'>Occupied</button>
                    <button className='legend' id='white'>Vacant and Clean</button>
                    <button className='legend' id='yellow'>Needs Cleaning</button>
                </div>
            </div>
            
            {isPopupVisible && (
                <div className="popup">
                    <div className="popup-content">
                        <span className="close" onClick={closePopup}>&times;</span>
                        <h2>Bed {selectedBed}</h2>
                        {patientsList[selectedBed.toString()]?.pName && <p>Patient Name: {patientsList[selectedBed.toString()]?.pName}</p>}
                        {patientsList[selectedBed.toString()]?.pGender && <p>Patient Gender: {patientsList[selectedBed.toString()]?.pGender}</p>}
                        {patientsList[selectedBed.toString()]?.pAge && <p>Patient Age: {patientsList[selectedBed.toString()]?.pAge}</p>}
                        <p>Room Status: {patientsList[selectedBed.toString()]?.status}</p>
                        
                        {patientsList[selectedBed]?.status === 'Occupied' && (
                            <button onClick={() => {
                                markForCleaning(selectedBed);
                                closePopup();
                        }}>Mark Room for Cleaning</button>
                        )}
                        {patientsList[selectedBed]?.status === 'Needs Cleaning' && (
                            <button onClick={() => {
                            endCleaning(selectedBed);
                            closePopup();
                         }}>Mark as Clean</button>
                        )}
                    </div>
                </div>
            )}
            
                <a href="/"><button>Return to Homepage</button></a>   
        </div>
    )
}

export default Map
