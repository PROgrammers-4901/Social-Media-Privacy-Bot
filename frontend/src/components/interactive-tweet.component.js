import axios from 'axios';
import React, { Component } from 'react';

export default class ContactForm extends Component {
    constructor(props) {
        super(props);

        this.onTrue = this.onTrue.bind(this);
        this.onFalse = this.onFalse.bind(this);
        this.onNext = this.onNext.bind(this);

        this.state = {
            tweet  : '',
            label  : false,
            answer : false
        }
    }

    
    componentDidMount() {
        // this gets called on start
        axios.get('http://localhost:5000/tweets/rand')
            .then(res => {
                this.setState({
                    tweet : res.data.contents,
                    label : res.data.label
                });
            })
            .catch(err => console.log("Cannot reach Database API: " + err));
    }

    onNext(e) {
        e.preventDefault();

        axios.get('http://localhost:5000/tweets/rand')
            .then(res => {
                this.setState({
                    tweet : res.data.contents,
                    label : res.data.label
                });
            })
            .catch(err => console.log("Cannot reach Database API: " + err));
    }

    onTrue(e) {
        e.preventDefault();
        if(this.state.label == true)
            this.setState({
                tweet: 'GOOD JOB!'
            });
        else
            this.setState({
                tweet: 'WRONG!'
            });
    }

    onFalse(e) {
        e.preventDefault();
        if(this.state.label == false)
            this.setState({
                tweet: 'GOOD JOB!'
            });
        else
            this.setState({
                tweet: 'WRONG!'
            });

    }

    render() {
        return (
            <div>
                <div>
                    <textarea placeholder="Example Tweet" 
                    rows="4" 
                    cols="50" 
                    id="Interactive-Tweets" 
                    name="interactiveTweets" 
                    readOnly
                    value={this.state.tweet}></textarea>
                </div>
                <div>
                    <button onClick={this.onTrue}> SPAM </button>
                    <button onClick={this.onFalse}> HAM </button>
                    <button onClick={this.onNext}> NEXT </button>
                </div>
            </div>
        )
    }
}