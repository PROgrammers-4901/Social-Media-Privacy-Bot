import React, { Component } from 'react';
import axios from 'axios';

export default class GetByHashtag extends Component {
    constructor(props) {
        super(props);

        this.onChangeHashtag = this.onChangeHashtag.bind(this); // bind 'this' to its respective function
        this.onSubmit = this.onSubmit.bind(this);

        this.state = {
            hashtag : ''
        }
    }

    // this gets called on start
    componentDidMount() {

    }

    onChangeHashtag(e) {
        this.setState({
            hashtag: e.target.value
        });
    }

    onSubmit(e) {
        e.preventDefault();

        // send request to Twitter API
        axios.get('http://localhost:5001/hashtag/' + this.state.hashtag)
            .then(res => {
                console.log(res.data)
                
                // redirect somewhere with results
            })
            .catch(err => console.log("Cannot reach Twitter API: " + err));
    }

    render() {
        return (
            <div>
                <br></br>
                <form onSubmit={this.onSubmit}>
                    <input type ="text"
                    placeholder="#Hashtag"
                    required
                    value={this.state.hashtag}
                    onChange={this.onChangeHashtag}
                    />
                </form>
            </div>
        )
    }
}