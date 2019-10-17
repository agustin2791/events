import React, { Component } from 'react'

class Event extends Component {
    constructor(props) {
        super(props)
        this.state = {
            event: props.event
        }
    }
    render() {
        return (
            <div className="card col-3" style={{margin: '3px'}}>
                <div className="card-body">
                    <h5 className="card-title">{this.state.event.eventName}</h5>
                    <p className="card-text">{this.state.event.eventDetails}</p>
                </div>
            </div>
        )
    }
}

export default Event