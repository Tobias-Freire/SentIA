package com.sentia.notification_service.repository;

import com.sentia.notification_service.model.FeedbackModel;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

import java.time.LocalDateTime;
import java.util.List;

public interface FeedbackRepository extends MongoRepository<FeedbackModel, String> {

    @Query(value = "{'general_classification': 'NEGATIVE'}")
    List<FeedbackModel> findAllNegativeClassifications();

    @Query(value = "{'general_classification': 'NEGATIVE'}", count = true)
    long countAllNegativeClassifications();

    @Query(value = "{'general_classification': 'NEGATIVE', 'datetime': { $gte:  ?0, $lt:  ?1} }")
    List<FeedbackModel> findAllNegativeClassificationsByDateRange(LocalDateTime start, LocalDateTime end);

    @Query(value = "{'general_classification': 'NEGATIVE', 'datetime': { $gte:  ?0, $lt:  ?1} }", count = true)
    long countNegativeClassificationsByDateRange(LocalDateTime start, LocalDateTime end);
}
