# Portfolio 5: Distributed and Cloud Database Exercise

## 1. Introduction

Portfolio 5 shows how cloud platforms and services can support the operations of West Haven Hotel & Suites. Some examples are Amazon Web Services (AWS), Cloudflare, and MongoDB Atlas. This portfolio builds on the MongoDB database from Portfolio 4 and shows how distributed database concepts can improve availability, scalability, and reliability.

A MongoDB Atlas cluster named `WestHavenCluster` was created under the West Haven Hotel project. Using a Python script, I migrated 40 booking documents into the `west_haven_hotel` database. These documents were stored in the `bookings` collection created within the database. The 40 documents contained booking information, including guest details, room information, payment records, and booking status.

## 2. Replication

A distributed database system uses replication to maintain copies of data across different database servers. In MongoDB Atlas, this is supported through a feature called replica sets. Instead of keeping just one copy of a database on a single server, replication allows multiple copies of the data to be maintained across different servers. This is important because different things can go wrong with a database system, including server failure or unexpected downtime. Having multiple copies helps reduce the risk of data loss and makes the database more reliable. This also reminds me of the 3-2-1 backup rule, which recommends keeping three copies of data, using two different storage types, and keeping one copy off-site.

Replica sets work by having a primary member and secondary members. The primary handles the main operations, while the secondary members keep copies of the data. If the primary becomes unavailable or fails, one of the secondary members can be selected to take over its role and continue handling operations. For West Haven Hotel, replication would help improve the availability of data in the database system while also protecting booking information against possible failures.

## 3. Consistency and Availability

Replication is useful when working with a database because it helps to keep the different servers updated when changes are made. However, the updates may not happen immediately, so the secondary servers might take some time to reflect the changes made on the primary server. This can cause them to lag. It is important to consider this when trying to access important information like room availability and booking status. For these kinds of operations, we need to choose the right read and write concerns to balance consistency, availability, and performance.

## 4. Sharding and Scalability

Sharding is similar to topology in networking. It is a technique used to distribute data across multiple servers or nodes. It supports horizontal scaling, especially when a database grows beyond the capacity of a single server. For West Haven Hotel, sharding could become useful if the business expands to different locations and the number of bookings increases beyond what a single server can handle. A shard key could be based on a common attribute, such as the hotel location or a unique identifier. Although I was not able to practise sharding during this practical exercise, I was still able to read about it and understand its usefulness in database system architecture.

## 5. Deployment Testing and Limitations

The MongoDB Atlas cluster was successfully created, and the 40 booking documents from the database developed in Portfolio 1 were imported into the collection. After this, I carried out a connectivity check to confirm that I could connect to the database and access the documents. However, I encountered a connectivity error during the check, which prevented me from completing the process successfully.

I tried to understand the error with the help of an AI tool, which helped me identify it as a connectivity issue. Since I could not resolve the problem and time was running out, I decided to focus on explaining the distributed database concepts I had learned through my research. This was also in line with the CA instructions, which allowed us to explain the concepts through research if we were unable to complete the practical deployment.

## 6. Conclusion

This exercise helped me understand how a distributed database system can be used in an organisation like West Haven Hotel & Suites and why it is important. MongoDB Atlas provided a platform to learn how a cloud-hosted database environment works and how different concepts such as replication, consistency, failover, and sharding support database systems. Although I was not able to practise all these concepts during the exercise, I was still able to understand their usefulness and how they can support the hotel's database operations.
