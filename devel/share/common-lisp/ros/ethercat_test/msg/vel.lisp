; Auto-generated. Do not edit!


(cl:in-package ethercat_test-msg)


;//! \htmlinclude vel.msg.html

(cl:defclass <vel> (roslisp-msg-protocol:ros-message)
  ((velocity
    :reader velocity
    :initarg :velocity
    :type (cl:vector cl:integer)
   :initform (cl:make-array 4 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass vel (<vel>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <vel>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'vel)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ethercat_test-msg:<vel> is deprecated: use ethercat_test-msg:vel instead.")))

(cl:ensure-generic-function 'velocity-val :lambda-list '(m))
(cl:defmethod velocity-val ((m <vel>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ethercat_test-msg:velocity-val is deprecated.  Use ethercat_test-msg:velocity instead.")
  (velocity m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <vel>) ostream)
  "Serializes a message object of type '<vel>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'velocity))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <vel>) istream)
  "Deserializes a message object of type '<vel>"
  (cl:setf (cl:slot-value msg 'velocity) (cl:make-array 4))
  (cl:let ((vals (cl:slot-value msg 'velocity)))
    (cl:dotimes (i 4)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<vel>)))
  "Returns string type for a message object of type '<vel>"
  "ethercat_test/vel")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'vel)))
  "Returns string type for a message object of type 'vel"
  "ethercat_test/vel")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<vel>)))
  "Returns md5sum for a message object of type '<vel>"
  "f8dbe9fe5f891a8fdba5d30d5afaa9f6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'vel)))
  "Returns md5sum for a message object of type 'vel"
  "f8dbe9fe5f891a8fdba5d30d5afaa9f6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<vel>)))
  "Returns full string definition for message of type '<vel>"
  (cl:format cl:nil "int32[4] velocity~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'vel)))
  "Returns full string definition for message of type 'vel"
  (cl:format cl:nil "int32[4] velocity~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <vel>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'velocity) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <vel>))
  "Converts a ROS message object to a list"
  (cl:list 'vel
    (cl:cons ':velocity (velocity msg))
))
