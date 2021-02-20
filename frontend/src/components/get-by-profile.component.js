import React, { Component } from 'react';

export default class GetByProfile extends Component {
    constructor(props) {
        super(props);

        this.onChangeProfile = this.onChangeProfile.bind(this); // bind 'this' to its respective function
        this.onSubmit = this.onSubmit.bind(this);

        this.state = {
            profileName : ''
        }
    }

    // this gets called on start
    componentDidMount() {

    }

    onChangeProfile(e) {
        this.setState({
            profileName: e.target.value
        });
    }

    onSubmit(e) {
        e.preventDefault();

        const profileName = {
            profileName: this.state.profileName
        }

        console.log(profileName);

        // send request to Twitter API

        // redirect somewhere with results
    }

    render() {
        return (
            <div>
                <br></br>
                <form onSubmit={this.onSubmit}>
                    <input type ="text"
                    placeholder="@Profile"
                    required
                    value={this.state.profileName}
                    onChange={this.onChangeProfile}
                    />
                </form>
            </div>
        )
    }
}