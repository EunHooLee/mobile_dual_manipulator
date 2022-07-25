// Auto-generated. Do not edit!

// (in-package mservo_msg.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class joint_data {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.pos = null;
    }
    else {
      if (initObj.hasOwnProperty('pos')) {
        this.pos = initObj.pos
      }
      else {
        this.pos = new Array(7).fill(0);
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type joint_data
    // Check that the constant length array field [pos] has the right length
    if (obj.pos.length !== 7) {
      throw new Error('Unable to serialize array field pos - length must be 7')
    }
    // Serialize message field [pos]
    bufferOffset = _arraySerializer.int32(obj.pos, buffer, bufferOffset, 7);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type joint_data
    let len;
    let data = new joint_data(null);
    // Deserialize message field [pos]
    data.pos = _arrayDeserializer.int32(buffer, bufferOffset, 7)
    return data;
  }

  static getMessageSize(object) {
    return 28;
  }

  static datatype() {
    // Returns string type for a message object
    return 'mservo_msg/joint_data';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '84fce591d749df1cf35b0205dc6eac71';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32[7] pos
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new joint_data(null);
    if (msg.pos !== undefined) {
      resolved.pos = msg.pos;
    }
    else {
      resolved.pos = new Array(7).fill(0)
    }

    return resolved;
    }
};

module.exports = joint_data;
