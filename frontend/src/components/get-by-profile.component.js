import React, { Component } from 'react';
import axios from 'axios';

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

        // send request to Twitter API
        axios.get('http://localhost:5001/username/' + this.state.profileName)
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