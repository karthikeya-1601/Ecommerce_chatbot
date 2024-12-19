const Message = ({ text, from }) => {
    return (
      <div className={`message ${from}`}>
        <p>{text}</p>
      </div>
    );
  };
  
  export default Message;
  