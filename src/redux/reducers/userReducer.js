import { FETCH_USERS_SUCCESS } from '../actions/userActions';

const userReducer = (state = [], action) => {
  switch (action.type) {
    case FETCH_USERS_SUCCESS:
      return action.payload;
    default:
      return state;
  }
};

export default userReducer;