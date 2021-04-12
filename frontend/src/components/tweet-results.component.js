import React, { Component } from 'react';
import axios from 'axios';

export default class TweetResults extends Component {
    constructor(props) {
        super(props);

        this.state = {
            tweet : "",
            label : -1,
            confidence : 0.0
        }
    }

    componentDidUpdate(prevProps) {
        if(prevProps.results !== this.props.results) {
            this.setState({
                tweet: this.props.results.tweet,
                label: this.props.results.label,
                confidence: this.props.results.confidence
            });
        }

        console.log(this.state);
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
                        value={this.state.label != -1 ? 
                            this.state.label == 0 ?
                                "HAM\n" + this.state.tweet + "\n\n Confidence: " + this.state.confidence :
                                "SPAM\n" + this.state.tweet+ "\n\n Confidence: " + this.state.confidence :
                            "Tweet Results"}></textarea>
                    </div>
                </form>
            </div>
        )
    }
}