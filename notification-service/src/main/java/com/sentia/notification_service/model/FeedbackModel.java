package com.sentia.notification_service.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document("feedback_analysis")
public class FeedbackModel {

    @Id
    private String id;

    private String feedback;
    private int stars_rank;
    private String predominant_emotion;
    private String general_classification;

    public FeedbackModel(String id, String feedback, int stars_rank, String predominant_emotion, String general_classification) {
        super();
        this.id = id;
        this.feedback = feedback;
        this.stars_rank = stars_rank;
        this.predominant_emotion = predominant_emotion;
        this.general_classification = general_classification;
    }
}
