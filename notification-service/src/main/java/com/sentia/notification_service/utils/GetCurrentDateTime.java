package com.sentia.notification_service.utils;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class GetCurrentDateTime {
    public static String getCurrentDateTime() {
        LocalDateTime now = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        return now.format(formatter);
    }
}
