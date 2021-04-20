import React from 'react';
import renderer from 'react-test-renderer';

import TweetBotNav from './tweetBotNav.component';

it('renders correctly', () => {
    const component = renderer.create(<TweetBotNav />).toJSON();
    expect(component).toMatchSnapshot();
});