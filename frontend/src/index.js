import React from 'react'
import ReactDOM from 'react-dom'
import Events from './components/Events'

function App() {
    return (
        <Events />
    )
}

ReactDOM.render(<App />, document.getElementById('app'))

module.hot.accept()