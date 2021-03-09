import React, { Component } from 'react';
import axios from 'axios';

export default class GetByTweet extends Component {
    constructor(props) {
        super(props);

        this.state = {
            message = ''
        }
    }

    // this gets called on start
    componentDidMount() {
        // somehow fill this in with the received tweet
    }

    render() {
        return (
            <div>
                <form>
                    <div>
                        <textarea placeholder="Tweet Results" 
                        rows="4" 
                        cols="50" 
                        id="ReceivedTweet" 
                        name="message" 
                        className="u-border-2 u-border-black u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle u-input-3" 
                        readOnly
                        value={this.state.message}></textarea>
                    </div>
                </form>
            </div>
        )
    }
}