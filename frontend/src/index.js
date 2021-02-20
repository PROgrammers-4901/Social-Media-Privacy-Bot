import React from 'react';
import ReactDOM from 'react-dom';

import GetByHashtag from './components/get-by-hashtag.component';
import GetByProfile from './components/get-by-profile.component';
import GetByTweet from './components/get-by-tweet.component';
import ContactForm from './components/contact-form.component';

ReactDOM.render(
  <React.StrictMode>
    <GetByHashtag />
  </React.StrictMode>,
  document.getElementById('getByHashtag')
);

ReactDOM.render(
  <React.StrictMode>
    <GetByProfile />
  </React.StrictMode>,
  document.getElementById('getByProfile')
);

ReactDOM.render(
  <React.StrictMode>
    <GetByTweet />
  </React.StrictMode>,
  document.getElementById('getByTweet')
);

ReactDOM.render(
  <React.StrictMode>
    <ContactForm />
  </React.StrictMode>,
  document.getElementById('contactForm')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
