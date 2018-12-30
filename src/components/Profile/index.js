import React, { Component } from 'react';
import { Card, Icon, Row, Col } from 'antd';
import 'antd/dist/antd.css';
import user from '../../data/user.json';

const { Meta } = Card;


class Profile extends Component {
  componentDidMount() {
    console.log(user)
  }

  render() {
    return (
      <Row justify='center'>
        <Col span={12}>
          <Card
            style={{ width: 300 }}
            cover={<img alt="example" src={ user.avatar_url } />}
            actions={[<Icon type="setting" />, <Icon type="edit" />, <Icon type="ellipsis" />]}
          >
            <Meta
              title={ user.name }
              description={ user.bio }
            />
          </Card>
        </Col>
      </Row>
    );
  }
}

export default Profile;