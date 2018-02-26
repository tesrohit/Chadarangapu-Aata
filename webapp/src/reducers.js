import * as boardActions from './actions';

const chessBoardInitialState = {
    board : [
      ["-1", "-1","-1", "-1","-1", "-1","-1", "-1", "-1", "-1"],
      ["-1", "W_R", "W_N", "W_B", "W_K", "W_Q", "W_B", "W_N", "W_R", "-1"],
      ["-1", "W_", "W_", "W_", "W_", "W_", "W_", "W_", "W_", "-1"],
      ["-1", "" , "" , "" , "" , "", "", "", "", "-1"],
      ["-1", "" , "" , "" , "" , "", "", "", "", "-1" ],
      ["-1", "" , "" , "" , "" , "", "", "", "", "-1" ],
      ["-1", "" , "" , "" , "" , "", "", "", "","-1" ],
      ["-1","B_", "B_", "B_", "B_", "B_", "B_", "B_", "B_","-1"],
      ["-1", "B_R", "B_N", "B_B", "B_K", "B_Q", "B_B", "B_N", "B_R", "-1"],
      ["-1", "-1","-1", "-1","-1", "-1","-1", "-1", "-1", "-1"],
    ],
    currentMoveInfo: {
        x1 : '',
        y1: '',
        x2: '',
        y2: ''
    },
    toMove: "W",
    moveInProgress: false,
    moveHistory: []
}

const chessboardReducer = (state=chessBoardInitialState, action) => {
    switch (action.type) {
        case boardActions.MAKE_MOVE_REQUESTED: {
            return {
                ...state, 
                moveInProgress: true
            }
        }

        case boardActions.MAKE_MOVE_SUCCEEDED: {
            let newBoard = JSON.parse(JSON.stringify(state.board));
            let {x1, y1, x2, y2} = {...state.currentMoveInfo};
            newBoard[x2][y2] = newBoard[x1][y1];
            newBoard[x1][y1] = "";
            return {
                ...state, 
                board:newBoard,
                currentMoveInfo: {
                    x1: "",
                    y1: "",
                    x2: "",
                    y2: ""
                },
                moveInProgress: false,
                toMove: state.toMove === "W"? "B": "W",
                moveHistory: state.moveHistory.concat(state.currentMoveInfo),
            }
        }

        case boardActions.MAKE_MOVE_FAILED: {
            return {
                ...state,
                currentMoveInfo: {
                    x1: "",
                    y1: "",
                    x2: "",
                    y2: ""
                },
                moveInProgress: false,
                error: action.payload.error
            }
        }

        case boardActions.SELECT_SQUARE: {
            // If source squares are unset, set them from action. Else keep them unchanged
            // If source squares x1, y1 are already set, then set the target values
            let newState = {
                ...state,
                currentMoveInfo: {
                    x1: state.currentMoveInfo.x1? state.currentMoveInfo.x1 : action.payload.x,
                    y1: state.currentMoveInfo.y1? state.currentMoveInfo.y1: action.payload.y,
                    x2: state.currentMoveInfo.x1 && state.currentMoveInfo.y1? action.payload.x: state.x2,
                    y2: state.currentMoveInfo.x1 && state.currentMoveInfo.y1? action.payload.y: state.y2
                }
            };
            return newState;
        }

        default:
            return state;
    }
}

export default chessboardReducer;