import React, { Component } from 'react';

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

        const hashtag = {
            hashtag: this.state.hashtag
        }

        console.log(hashtag);

        // send request to Twitter API

        // redirect somewhere with results
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