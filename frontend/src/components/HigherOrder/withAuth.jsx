import React from "react";
import {Redirect} from "react-router-dom";
import SideBar from "../SideBar";
import Cookies from 'js-cookie';
import store from '../../store/index.js';

export default function withAuth(Component, navId) {
    return class extends Component {
        render() {
            const isLoggedIn = store.getState().loginReducers.isLoggedIn || Cookies.get("userPass");
            if (isLoggedIn) {
                return (
                    <div>
                    	<SideBar currentLoc={navId}/>
                        <Component {...this.props} />
                    </div>
                );
            } else {
                return (
                    <Redirect to={"/"}/>
                );
            }
        }
    };
}
