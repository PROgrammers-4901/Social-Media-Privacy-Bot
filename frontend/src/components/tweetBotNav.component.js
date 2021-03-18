import React, { Component } from 'react';
import axios from 'axios';

export default class TweetBotNav extends Component {
    constructor(props) {
        super(props);

        this.onChangeInput = this.onChangeInput.bind(this); // bind 'this' to its respective function
        this.onChangeSearchFunction = this.onChangeSearchFunction.bind(this);
        this.onSubmit = this.onSubmit.bind(this);

        this.state = {
            input: '',
            function: "Tweet",
        }
    }

    // this gets called on start
    componentDidMount() {

    }

    onChangeInput(e) {
        this.setState({
            input: e.target.value
        });
    }

    onChangeSearchFunction(e) {
        this.setState({
            function: e.target.value
        });
    }

    onSubmit(e) {
        e.preventDefault();

        console.log(this.state);

        switch (this.state.function) {
            default:
            case "Tweet": this.searchByURL();
                break;
            case "Account": this.searchByAccount();
                break;
            case "Hashtag": this.searchByHashtag();
                break;
        }
    }

    searchByURL() {
        // break apart URL
        const tweet_id = this.state.input.match(/status\/(\d+)$/); // regex is one or more digits at the end of the URL followed by status/

        if (tweet_id != null) {
            axios.get('http://localhost:5001/tweet_id/' + tweet_id[1])
                .then(res => {
                    console.log(res.data)

                    // redirect somewhere with results
                })
                .catch(err => this.setState({ input: 'Failed to Find Tweet' }));
        }
        else {
            this.setState({
                input: 'Invalid URL'
            })
        }
    }

    searchByAccount() {
        // send request to Twitter API
        axios.get('http://localhost:5001/username/' + this.state.input)
            .then(res => {
                console.log(res.data)
                
                // redirect somewhere with results
            })
            .catch(err => console.log("Cannot reach Twitter API: " + err));
    }

    searchByHashtag() {

        // send request to Twitter API
        axios.get('http://localhost:5001/hashtag/' + this.state.input)
            .then(res => {
                console.log(res.data)
                
                // redirect somewhere with results
            })
            .catch(err => console.log("Cannot reach Twitter API: " + err));
    }

    render() {
        return (
            <nav className="navbar navbar-dark navbar-expand bg-dark navigation-clean">
                <a className="navbar-brand" href="#"><i>PROgrammers</i></a>
                <div className="container align-middle">
                    <input 
                     type="text"
                     className="form-control"
                     placeholder="Search..."
                     value={this.state.input}
                     onChange={this.onChangeInput}
                     onSubmit={this.onSubmit}
                     />
                    <select className="custom-select"
                     onChange={this.onChangeSearchFunction}
                     value={this.state.function}>
                        <option value="Tweet">Search by Tweet</option>
                        <option value="Account">Search by Account</option>
                        <option value="Hashtag">Search by Hashtag</option>
                    </select>
                    <button 
                     className="btn btn-primary mx-2"
                     data-bss-hover-animate="pulse"
                     type="button"
                     onClick={this.onSubmit}
                     >Search!</button>
                </div>
            </nav>
        )
    }
}