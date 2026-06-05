import Header from "./components/Header";
import Footer from "./components/Footer";
import Greet from "./components/greet";

function App() {
  const myClg="MIT ADTU"
  const myName="Aarush Parate";
  const mySpeed=55;
  return (
    <>
      <Header />

      <Greet name="Everybody"/>
      <h3>This is a simple React application</h3>
      <h3>My Name is {myName} </h3>
      <p>i am {16+4} years old</p>
      <p>My College Name is {myClg}</p>
      <p>My speed is {mySpeed} km/hr</p>
      {mySpeed<75 ?<p style={{color: 'green'}}>I am Safe</p>:<p style={{color: 'red'}}>I am Dangerous</p>}

      <Footer />
    </>
  )
}

export default App;