import React from 'react';
import {connect} from 'react-redux';
import {symbols}  from "./symbols";
import * as boardActions from './actions';

const Square = (props) => {
  let pieceClass = "emptySquare";  // This will decide which piece is in the square

  let pieceSymbols = {};
  Object.keys(symbols).forEach((key) => {
    pieceSymbols[symbols[key]] = key;
  });

  if(props.piece) {
    let color, pieceSymbol;
    [color, pieceSymbol] = props.piece.split("_");
    if(color) {
      color === "W" ? pieceClass = "white" :  pieceClass= 'black';
      pieceClass += pieceSymbols[pieceSymbol]
    }
  }
  let squareClass = `square ${pieceClass} `;
  
  if(props.isSourceSquare || props.isTargetSquare) {
    squareClass += "selectedSquare";
  }

  return (
    <span 
      className={squareClass}
      onClick={props.handleSquareClick}
    >
    </span>
  );
}

const Row = (props) => {
  let squares = [];

  for(let col=1;col<=8;col++){
    let isSourceSquare = (
      props.sourceSquare.x === props.row && 
      props.sourceSquare.y === col
    );

    squares.push(
      <Square 
        key={`${props.row}-${col}`} 
        row={props.row} 
        col={col} 
        piece={props.board[props.row][col]}
        isSourceSquare={isSourceSquare}
        isTargetSquare={isSourceSquare}
        handleSquareClick={() => {props.handleSquareClick(props.row, col)}}
      />
    )
  }

  return (
  <div className="row">
    {squares}
  </div>)
}

class ChessBoard extends React.Component{
  componentDidUpdate() {
    if(this.props.currentMoveInfo.x1 && this.props.currentMoveInfo.y1
      && this.props.currentMoveInfo.x2  && this.props.currentMoveInfo.y2){
      this.props.makeMove(
        this.props.currentMoveInfo.x1,
        this.props.currentMoveInfo.y1,
        this.props.currentMoveInfo.x2, 
        this.props.currentMoveInfo.y2);
    }
  }

  renderMoveHistory() {
    let renderedHistory = [];
    for(let index=this.props.moveHistory.length-1; index>=0; index-=1) {
        let element = this.props.moveHistory[index];
        renderedHistory.push(
          <li key={index}>
            {String.fromCharCode('a'.charCodeAt(0)+ element.y1 -1)}{element.x1} 
            => 
            {String.fromCharCode('a'.charCodeAt(0)+ element.y2 -1)}{element.x2}
          </li>
        )
    }
    return <ol reversed> {renderedHistory} </ol>;
  }

  render() {
    let rows = [];

    for(let row=8;row>=1;row--){
      rows.push(
        <Row 
          key={row} 
          row={row}
          board={this.props.board}
          sourceSquare={{x: this.props.currentMoveInfo.x1, y: this.props.currentMoveInfo.y1}}
          targetSquare={{x: this.props.currentMoveInfo.x2, y: this.props.currentMoveInfo.y2}}
          handleSquareClick={(row, col) => {this.props.squareClicked(row, col)}}
        />
      );
    }

    return (
    <div className="row">
      <div className="column unimplemented">
          <div> Player info </div>
          <div> Dead pieces </div>
      </div>
      <div className="column">
          <div className="unimplemented">
            <div className="menu">
              Game menu (New game, Resume, game level etc.)
            </div>
          </div>
          <div className="column boardDisplay">
              {rows}
          </div>
          <div className="row unimplemented">
            <button disabled> undo </button> 
            <button disabled> redo </button>
            <button disabled> resign </button>
            <button disabled> claim draw </button>
          </div>
      </div>

      <div>
        <div className="unimplemented"> Timer </div>
        <div> 
          <h4> Move history</h4>
          <hr />
          <div className="overflowingBox">{this.renderMoveHistory()}</div>
        </div>
      </div>
  </div>
    )
  }
}

const mapStateToProps = state => {
  return {
    board: state.board,
    currentMoveInfo: state.currentMoveInfo,
    moveHistory: state.moveHistory
  }
};

const mapDispatchToProps = dispatch => {
  return {
    squareClicked: (x, y) => {
      console.log("Square clicked: ",x, y);
      dispatch({
        type: boardActions.SELECT_SQUARE,
        payload: {
          x, 
          y
        }
      });
    },
    makeMove: (x1, y1, x2, y2) => {
      console.log("Making move: ",
      "From: (", x1, y1, ") ",
      "To: (", x2, y2,")");
      // TODO: make it a redux thunk when we integrate backend call
      // We then need to dispatch MAKE_MOVE_REQUESTED 
      dispatch({
        type: boardActions.MAKE_MOVE_SUCCEEDED,
        payload: {
          x1, y1, x2, y2
        }
      });
    }
  }
};

export default connect(mapStateToProps, mapDispatchToProps)(ChessBoard);