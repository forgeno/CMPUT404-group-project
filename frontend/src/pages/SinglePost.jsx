import React, { Component } from 'react';
import StreamFeed from '../components/StreamFeed';
import store from '../store/index.js';
import './styles/SinglePost.css';

class SinglePost extends Component {	

	render() {
		const urlPath = "/api/posts/" + this.props.match.params.postId
		const storeItems = store.getState().loginReducers;
		return(	
			<div className="pusher">
				<h1 className="singlePostHeader"> {"POST: " + this.props.match.params.postId} </h1>
				<StreamFeed storeItems={storeItems} urlPath={urlPath} />
			</div>
			)
    }
}

export default SinglePost;
