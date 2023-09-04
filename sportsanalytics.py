#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 17:54:16 2023

@author: antheasago
"""

import cv2

# Load the video
video_path = 'path_to_your_video.mp4'
cap = cv2.VideoCapture(video_path)

# Initialize object tracker
tracker = cv2.TrackerCSRT_create()

# Initialize player statistics
player_stats = {}

# Loop through video frames
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Here you would implement player detection using object detection models
    
    # Assuming you have detected players, loop through each detected player
    for player_bbox in detected_players:
        player_id = player_bbox['id']  # An identifier for the player
        
        # If player is new, initialize tracker
        if player_id not in player_stats:
            player_stats[player_id] = {
                'frames_played': 0,
                'distance_covered': 0,
                # Add more statistics you want to collect
            }
            tracker.init(frame, player_bbox['bbox'])
        
        # Update tracker
        success, bbox = tracker.update(frame)
        
        if success:
            # Update player statistics
            player_stats[player_id]['frames_played'] += 1
            # Calculate player movement distance and update the 'distance_covered' field
            # You would need to implement distance calculation based on player's previous and current positions
        
        # Draw player bbox on the frame
        x, y, w, h = [int(coord) for coord in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Display the frame with player bounding boxes
    cv2.imshow('Player Tracking', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()

# Print the collected player statistics
for player_id, stats in player_stats.items():
    print(f"Player {player_id} statistics: {stats}")
