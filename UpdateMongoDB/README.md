Mongo Management

Managing the DB is happening throw MongoDB singelton class, this class is wrapper for MongoClient provided by pymongo

The main idea of this class is to sync the DB with the data gathered by scrapper
The reviews collected are saved in JSON format, and then proccesed and inserted into MongoDB






Processing
The data processing is handled by glyph_process and NRC_Processor, this file containes all methoed used for creating glyphes stored in the DB

