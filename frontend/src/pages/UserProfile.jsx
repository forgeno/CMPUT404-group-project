import React, { Component } from 'react';
import 'semantic-ui-css/semantic.min.css';
import SideBar from '../components/SideBar';
import ProfileBubble from '../components/ProfileBubble';
import './styles/Profile.css';
import { Container } from 'semantic-ui-react';
import { Tab } from 'semantic-ui-react';
import { Table } from 'semantic-ui-react';
import { Icon } from 'semantic-ui-react';
import { Button } from 'semantic-ui-react';
import HTTPFetchUtil from '../util/HTTPFetchUtil.js';
import {connect} from 'react-redux';
import store from "../store/index";
class Profile extends Component {	

	constructor(props) {
        super(props);
		this.state = {
            profiledata: []
        };
        this.getProfile = this.getProfile.bind(this);
        this.showPanes = this.showPanes.bind(this);
    }

    showPanes = () => {
        return (
            [
                { menuItem: 'About', render: () => <Tab.Pane>
                    <Table basic='very'>
                    <Table.Header>
                        <Table.Row>
                            <Table.HeaderCell>Bio</Table.HeaderCell>
                            <Table.HeaderCell></Table.HeaderCell>
                        </Table.Row>
                        <Table.Row>
                            <Table.Cell>{this.state.profiledata.bio}</Table.Cell>
                        </Table.Row>
                    </Table.Header>
                    </Table>

                    <Table basic='very'>    
                        <Table.Header>
                        <Table.Row>
                            <Table.HeaderCell>Basic Information</Table.HeaderCell>
                            <Table.HeaderCell></Table.HeaderCell>
                        </Table.Row>
                        </Table.Header>

                        <Table.Body>
                        <Table.Row>
                            <Table.Cell>Name</Table.Cell>
                            <Table.Cell>{this.state.profiledata.firstName} {this.state.profiledata.lastName}</Table.Cell>
                        </Table.Row>
                        <Table.Row>
                            <Table.Cell>Github</Table.Cell>
                            <Table.Cell><a href={this.state.profiledata.github}>{this.state.profiledata.github}</a>
                            </Table.Cell>
                        </Table.Row>
                        <Table.Row>
                            <Table.Cell>Email</Table.Cell>
                            <Table.Cell>{this.state.profiledata.email}
                            </Table.Cell>
                        </Table.Row>
                        </Table.Body>
                    </Table>
                </Tab.Pane> },
                { menuItem: 'Posts', render: () => <Tab.Pane>Stream component goes here</Tab.Pane> },
                { menuItem: 'Friends', render: () => <Tab.Pane>Friend List component goes here</Tab.Pane> },
              ]
        )
    }

    // handleClick(e) {
    //     path = "/api/friendrequest", data = "", content_type = "application/json"
    //     HTTPFetchUtil.sendPostRequest()
    // }

    // handleSubmit() {
    //     const requireAuth = true,
    //     urlPath = "api/author/"
    //     requestBody = {

    //     }
    //     }

    componentDidMount() {
        this.getProfile();
    }

    getProfile() {
        var urlPath = "/api/author/"
        var authorId = store.getState().loginReducers.userId.split("thor/");
        const path = urlPath + authorId[1], requireAuth = true;
        HTTPFetchUtil.getRequest(path, requireAuth)
        .then((httpResponse) => {
            if (httpResponse.status === 200) {
                httpResponse.json().then((results) => {
                    this.setState( {
                        profiledata: results
                    })
                })
            }
        });
    }

	render() {
	    return(
		    <Container>
                <SideBar/>
                    <div className="profile">
                        <br/>
                        <ProfileBubble
                        profileBubbleClassAttributes={"ui centered top aligned circular bordered small image"}/>
                        <br/><div className="profile-username">{this.state.profiledata.displayName}     </div>
                            <Button positive>
                                <Icon name= "user plus" />
                                Request Friend
                            </Button>
                    <div>
                        <Tab panes={this.showPanes()}></Tab>
                    </div>
                    </div>
            </Container>
	    )
    }
}


const mapStateToProps = (state) => {
    return {
        userId: state.userId,
    }
}

export default connect(mapStateToProps)(Profile);