import {useState} from "react";

export default function MyHooksDemo(){
    const [count, setCount] = useState(0);

    return(
        <div>
            <h2>My counter is: {count}</h2>
            <button onClick={() => setCount(count + 1)}>Increment</button>
            <button onClick={() => setCount(count - 1)}>Decrement</button>  
        </div>
    )
}