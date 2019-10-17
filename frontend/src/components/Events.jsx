import React, { Component } from 'react'
import Event from './events/Event'
import axios from 'axios'
// import events from '../eventsInfo'

class Events extends Component {
    constructor() {
        super()
        this.state = {
            events: []
        }
    }

    componentDidMount() {
        axios.get('http://localhost:5000/api/events')
            .then(res => {
                return res.data.results
            })
            .then(data => {
                this.setState({events: data})
            })
    }

    render() {
        let eventsArray = this.state.events.map(event => {
            return <Event key={event.id} event={event} />
        });
        return (
            <div className="row">
                {eventsArray}
            </div>
        )
    }
}

export default Events