import React, { useState, useEffect } from "react";
import logo from './logo.svg';
import './App.css';

import LoadingScreen from './components/LoadingScreen';
import Title from './components/Title';

function App() {
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Simulate some loading time (replace with your actual loading logic)
    setTimeout(() => {
      setIsLoading(false);
    }, 2000); // Set timeout for 2 seconds (adjust as needed)
  }, []);


  return (
    <div className="App bg-bg1 h-svh w-svw flex flex-col px-[5%] font-mono overflow-hidden">
      <Title />
      {isLoading && <LoadingScreen />}
    </div>
  );
}

export default App;
