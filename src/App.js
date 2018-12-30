import React, { Component } from 'react';
import { Layout } from 'antd';
import 'antd/dist/antd.css';

import Profile from './components/Profile';

const { Footer, Content } = Layout;

class App extends Component {
  render() {
    return (
      <Layout>
        <Content>
          <Profile />
        </Content>
        <Footer>Footer</Footer>
      </Layout>
    );
  }
}

export default App;
