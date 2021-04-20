import React from 'react';
import renderer from 'react-test-renderer';

import TweetResults from './tweet-results.component';

it('renders correctly given no input', () => {
    const component = renderer.create(<TweetResults />).toJSON();
    expect(component).toMatchSnapshot();
});

it('renders correctly given results', () => {
    const output = {
        tweet: "1383923017923760131",
        label: "1",
        confidence: "1"
    };

    const component = renderer.create(<TweetResults results = {output} />).toJSON();
    expect(component).toMatchSnapshot();
});