import React from "react";
import ReactDOM from "react-dom";
import Text from "react-text-typing";

const App = () => <Text text="Example Text" showBlink={true} component="h1" />;

ReactDOM.render(<App />, document.getElementById("root"));