import { useState } from 'react'

function PatientForm() {
    const [pName, setPName] = useState('');
    const [pGender, setPGender] = useState('select');
    const [pAge, setPAge] = useState(0);
    const [isoContagious, setIsoContagious] = useState(true);
    const [isoPalliative, setIsoPalliative] = useState(true);
    const [superCog, setSuperCog] = useState(true);
    const [superAgg, setSuperAgg] = useState(true);
    const [noMixedReligious, setNoMixedReligious] = useState(true);
    const [fetchIP, setFetchIP] = useState(false);
    
    const changeHandler = (e) => {
        console.log('in change handler, e.name, e.target.value', e.target.name, e.target.value);
        switch(e.target.name) {
            case 'isoCont':
                setIsoContagious(e.target.value);
                break;
            case 'palliative':
                setIsoPalliative(e.target.value);
                break;
            case 'cognitive':
                setSuperCog(e.target.value);
                break;
            case 'aggression':
                setSuperAgg(e.target.value);
                break;
            case 'religious':
                setNoMixedReligious(e.target.value);
                break;
            default:
                break;
        }
    }

    const submitHandler = (e) => {
        e.preventDefault();
        const patientInfo = {pName, pGender, pAge, isoContagious, isoPalliative, superCog, superAgg, noMixedReligious};
        
        setFetchIP(true);

        fetch('ENDPOINT', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify(patientInfo)
        }).then(() => {
            console.log("information posted successfully");
            setFetchIP(false);
        })
        
    }

    return (
        <div>
            {(fetchIP) ? (
            
                <p>Loading...</p>
              ) : (
                <form onSubmit={e => submitHandler(e)}>
           
            <label htmlFor="pname"><b>Patient Name:</b>
                <input 
                    type="text" 
                    id="pname"
                    value={pName}
                    onChange = {e => setPName(e.target.value)}
                />
            </label><br /><br />
            
            <label><b>Patient Gender:</b></label><br />
                <select 
                    id="gender"
                    value={pGender}
                    onChange ={e => setPGender(e.target.value)}>
                    <option value="select">Select</option>
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                    <option value="other">Other</option>
                </select>
            <br /><br />
            
            <label htmlFor="age"><b>Patient Age:</b>
                <input 
                    type="number" 
                    id="age" 
                    value={pAge}
                    onChange = {e => setPAge(e.target.value)}
                    />
            </label><br /><br />
            
            <label><b>Does this patient need to be isolated for any of the following reasons?:</b> <em>communicable disease or epidemiologically significant organism</em>
            <br></br>
                <label htmlFor="yes-isolated-contagious">Yes</label><input 
                    type="radio" 
                    name='isoCont'
                    id="yes-isolated-contagious"
                    value={true}
                    onChange = {(e) => changeHandler(e)}
                    /><br></br>
                <label htmlFor="no-isolated-contagious">No</label><input 
                    type="radio" 
                    name='isoCont'
                    id="no-isolated-contagious"
                    value={false}
                    onChange = {(e) => changeHandler(e)}/>
            </label><br /><br />
            
            <label><b>Does this patient need to be isolated for any of the following reasons?:</b> <em>requires palliative care or a clinical issue indicates privacy is required</em>
            <br></br>
                <label htmlFor="yes-isolated-palliative">Yes</label><input 
                    type="radio" 
                    name='palliative'
                    id="yes-isolated-palliative"
                    value={true}
                    onChange = {(e) => changeHandler(e)}/><br></br>
                <label htmlFor="no-isolated-palliative">No</label><input 
                    type="radio" 
                    name='palliative'
                    id="no-isolated-palliative"
                    value={false}
                    onChange = {(e) => changeHandler(e)}/>
            </label><br /><br />
            
            <label><b>Does this patient require enhanced supervision for any of the following reasons?:</b> <em>fall risk, cognitive functioning, etc.</em>
            <br></br>
                <label htmlFor="yes-enhanced-cognitive">Yes</label><input 
                    type="radio" 
                    name='cognitive'
                    id="yes-enhanced-cognitive"
                    value={true}
                    onChange = {(e) => changeHandler(e)}/><br></br>
                <label htmlFor="no-enhanced-cognitive">No</label><input 
                    type="radio" 
                    name='cognitive'
                    id="no-enhanced-cognitive"
                    value={false}
                    onChange = {(e) => changeHandler(e)}/>
            </label><br /><br />

            <label><b>Does this patient require enhanced supervision for any of the following reasons?:</b> <em>aggression, behavioural risks, etc.</em>
            <br></br>
                <label htmlFor="yes-enhanced-aggression">Yes</label><input 
                    type="radio" 
                    name='aggression'
                    id="yes-enhanced-aggression"
                    value={true}
                    onChange = {(e) => changeHandler(e)}/><br></br>
                <label htmlFor="no-enhanced-aggression">No</label><input 
                    type="radio" 
                    name='aggression'
                    id="no-enhanced-aggression"
                    value={false}
                    onChange = {(e) => changeHandler(e)}/>
            </label><br /><br />

            <label><b>Is this patient unable to be in mixed gender accomodations for any of the following reasons?:</b> <em>cultural or religious beliefs</em>
            <br></br>
                <label htmlFor="yes-mixed-religious">Yes</label><input 
                    type="radio" 
                    name='religious'
                    id="yes-mixed-religious"
                    value={true}
                    onChange = {(e) => changeHandler(e)}/><br></br>
                <label htmlFor="no-mixed-religious">No</label><input 
                    type="radio" 
                    name='religious'
                    id="no-mixed-religious"
                    value={false}
                    onChange = {(e) => changeHandler(e)}/>
            </label><br /><br />
            <button>Submit</button>
        </form>
              )}
        </div>
        
        

    )


}

export default PatientForm;