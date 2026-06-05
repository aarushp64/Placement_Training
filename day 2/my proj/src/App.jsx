import './App.css';
import Cards from './components/Cards';
import Rohit from "./assets/rohit.jpg";
import Virat from "./assets/virat.jpg";
import Dhoni from "./assets/dhoni.jpg";
import Gayle from "./assets/gayle.jpg";
import Abde from "./assets/abd.jpg";
import Raina from "./assets/raina.jpg";
import MyHooksDemo from './components/MyHooksDemo';


function App() {
  return (
    <>
      <h1>IPL GOATS</h1>
      <Cards pic={Rohit} title="Rohit Sharma" desc="MI captain" />
      <Cards pic={Virat} title="Virat Kohli" desc="RCB captain" />
      <Cards pic={Dhoni} title="Mahendra Singh Dhoni" desc="CSK captain" />
      <Cards pic={Gayle} title="Chris Gayle" desc="WI batsman" />
      <Cards pic={Abde} title="AB de Villiers" desc="RCB batsman" />
      <Cards pic={Raina} title="Suresh Raina" desc="CSK batsman" />
      <MyHooksDemo />
    </>
  );
}

export default App;