import React, { Component } from 'react';
import { Tweet } from 'react-twitter-widgets';

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
                confidence: this.props.results.confidence,
            });            
        }
    }

    getOpeningText() {
        if(this.state.label != -1)
        {
            switch (this.state.type) {
                default:
                case "Tweet": 

                break;

                case "Account": 
                case "Hashtag": 
                break;
            }
        }
    }

    render() {

        let opening = <p className="my-0 py-0 text-light">This {this.state.type} is...</p>;
        let score;
        let confidence = <figcaption className="blockquote-footer"> Confidence: {(this.state.confidence*100).toFixed(0) + "%"} </figcaption>

        switch (this.state.type) {
            case "Tweet": 
                score = <h2 className={"my-0 py-0 " + (this.state.label == 0 ? "text-success" : "text-danger")}>{(this.state.label == 0 ? " HAM!" : " SPAM!")}</h2>;
            break;

            case "Account": 
            case "Hashtag": 
                score = <h2 className="my-0 py-0 text-danger"> {(this.state.label*100).toFixed(0) + "% spam!"} </h2>;
            break;

            default:
            break;
        }

        return (
            <div>
                <figure className="text-center">
                    <blockquote className="blockquote">
                        {this.state.type !== "Empty" ? opening : null}

                        {this.state.type !== "Empty" ? score : null}                        
                    </blockquote>
                    {this.state.type !== "Empty" ? 
                    <Tweet
                        tweetId={this.state.tweet}
                        renderError={(_err) => null}
                        options={{ align: "center", theme: "dark"}}
                    /> : null}
                    {this.state.type !== "Empty" ? confidence : null}
                </figure>
            </div>
        )
    }
}