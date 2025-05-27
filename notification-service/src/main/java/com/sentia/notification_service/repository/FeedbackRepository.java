package com.sentia.notification_service.repository;

import com.sentia.notification_service.model.FeedbackModel;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

import java.util.List;

public interface FeedbackRepository extends MongoRepository<FeedbackModel, String> {

    @Query(value = "{'general_classification': 'NEGATIVE'}")
    List<FeedbackModel> findAllNegativeClassifications();

    @Query(value = "{'general_classification': 'NEGATIVE'}", count = true)
    long countAllNegativeClassifications();

}
