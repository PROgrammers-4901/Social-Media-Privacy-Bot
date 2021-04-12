import React, { Component } from 'react';
import axios from 'axios';

export default class TweetResults extends Component {
    constructor(props) {
        super(props);

        this.state = {
            type: "Empty",
            tweet : "",
            label : -1,
            confidence : 0.0
        }
    }

    componentDidUpdate(prevProps) {
        if(prevProps.results !== this.props.results) {
            this.setState({
                type: this.props.results.type,
                tweet: this.props.results.tweet,
                label: this.props.results.label,
                confidence: this.props.results.confidence
            });
        }

        console.log(this.state);
    }

    writeOutput() {
        var results = "";

        if(this.state.label != -1)
        {

            switch (this.state.type) {
                default:
                case "Tweet": 
                    if(this.state.label == 0)
                        results += "HAM\n";
                    else
                        results += "SPAM\n";

                    results += this.state.tweet;

                    results += "\n\n Confidence: " + (this.state.confidence*100).toFixed(0) + "%";
                    break;

                case "Account": 
                case "Hashtag": 
                    results += "This "+ this.state.type +" is " + (this.state.label*100).toFixed(0) +"% spam!\n\n";
                    results += "Spammiest Tweet:\n" + (this.state.tweet) + "\n\nConfidence: " + this.state.confidence;
                    break;
            }
        }
        else
        {
            results = "Tweet results";
        }

        return results;
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
                        value={this.writeOutput()}></textarea>
                    </div>
                </form>
            </div>
        )
    }
}